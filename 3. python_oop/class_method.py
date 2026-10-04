class Document:
  def __init__(self,text,source):
    self.text = text
    self.source=source
  def teacher_info(self):
      print(f"Rohan sir best subject is : {self.text}")
      return True

lang1 = Document('python','online source')

lang2 = Document('java','hand written notes')

print(lang1.teacher_info())