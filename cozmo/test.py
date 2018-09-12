import cozmo

def say_hello(robot: cozmo.robot.Robot):
    robot.say_text("hellooooooooooo").wait_for_completed()

cozmo.run_program(say_hello)



