from experta import*
class StudentFacts(Fact):
	pass
class CareerExpertSystem(KnowledgeEngine):
	@Rule(StudentFacts(likes="Maths"),StudentFacts(likes="Physics"))
	def mechanical(self):
		print("Suggested Career path: Mechanical Engineering")
		
	@Rule(StudentFacts(likes="Programming"),StudentFacts(likes="Maths"))
	def computer(self):
		print("Suggested Career path: Computer Engineering")
		
	@Rule(StudentFacts(likes="Biology"),StudentFacts(likes="Chemistry"))
	def biotech(self):
		print("Suggested Career path: Biotechnology")	
		
	@Rule(StudentFacts(likes="Circuits"),StudentFacts(likes="Maths"))
	def electronics(self):
		print("Suggested Career path: Electronics Engineering")	
		
def main():
	engine = CareerExpertSystem()
	engine.reset()
	print("Welcome to the Career Expert System!")
	
	interests = input("Enter your interests separated by commas:").split(",")
	
	for interest in interests:
		engine.declare(StudentFacts(likes=interest.strip()))
	engine.run()
	
if __name__ == "__main__":
	main()				
	
