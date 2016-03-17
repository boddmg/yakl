import trollius
from trollius import From

import pygazebo
import pygazebo.msg.joint_cmd_pb2
import pygazebo.msg.pid_pb2

@trollius.coroutine
def publish_loop():
    manager = yield From(pygazebo.connect())

    publisher = yield From(
        manager.advertise('/gazebo/default/simple_arm_0/joint_cmd',
                          'gazebo.msgs.JointCmd'))

    message = pygazebo.msg.joint_cmd_pb2.JointCmd()
    message.name = 'simple_arm_0::arm_shoulder_pan_joint'
    message.position.target = 3

    yield From(publisher.publish(message))
    yield From(trollius.sleep(0.5))
    yield From(publisher.publish(message))
    yield From(trollius.sleep(0.5))

loop = trollius.get_event_loop()
loop.run_until_complete(publish_loop())