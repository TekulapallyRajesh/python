class India:
    def show_info(self):
        print("delhi")
class Telangana(India):
    def language(self):
        print("telugu")
class Andhra(Telangana):
    def cm(self):
        print("chandra babu naidu")



a=India()
b=Telangana()
c=Andhra()
c.show_info()
c.language()
c.cm()