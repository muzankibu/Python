# importing cProfile
import cProfile


def f():
	print("hello")


cProfile.run('f()')
