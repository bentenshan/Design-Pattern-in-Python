class Subject(object):
	def open(self):
		print "open channel"

	def close(self):
		print "close channel"

	def send(self):
		print "sending Data"

	def recv(self):
		print "receiving Data"

class Proxy(object):
	interfaces = ["open", "send", "close"]

	def __init__(self):
		self.__subject = Subject()

	def hasAuth(self, name):
		return name in self.interfaces

	def __getattr__(self, name):
		if not self.hasAuth(name): raise "need %s authentication" % name

		return getattr(self.__subject, name)


if __name__ == "__main__":
	proxy = Proxy()
	proxy.open()
	proxy.send()
	proxy.recv()





