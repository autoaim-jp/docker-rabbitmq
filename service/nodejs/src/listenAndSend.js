const amqplib = require('amqplib')

const main = async () => {
  const queue = 'greet2'
  const conn = await amqplib.connect('amqp://root:password@rabbitmq:5672')

  const ch1 = await conn.createChannel()
  await ch1.assertQueue(queue)

  // Listener
  ch1.consume(queue, (msg) => {
    if (msg !== null) {
      console.log('Recieved:', msg.content.toString())
      ch1.ack(msg)
    } else {
      console.log('Consumer cancelled by server')
    }
  })

  // Sender
  const ch2 = await conn.createChannel()

  setInterval(() => {
    ch2.sendToQueue(queue, Buffer.from('something to do'))
  }, 5 * 1000)
}

main()

