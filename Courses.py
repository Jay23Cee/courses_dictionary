courses = { "Math":["Algebra","Geometry", "Statistic", "Trig"],"Co Sci" :["Python", "Java", "C++"]      }



def getClass(mclass):
		if mclass in courses:
			for cclass  in courses[mclass]:
					print(cclass)
		
          


getClass("Math")
