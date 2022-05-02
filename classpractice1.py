class Employe():
	def __init__(self, first,last,pay):
		self.first = first
		self.last = last
		self.email = first+ '.' + last + '@company.com'
		self.pay = pay

	def fullname(self):
		return '{} {}'.format(self.first , self.last)

employe1 = Employe('Jose','Castellon',5000)
employe2 = Employe('Maria','Martinez',4000)

print(employe2.fullname())
print(Employe.fullname(employe2))

