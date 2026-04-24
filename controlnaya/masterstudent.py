from student import Student
class MasterStudent(Student):
    def __init__(self, name: str, gpa: float, year: int, thesis_topic: str, supervisor: str):
        super().__init__(name, gpa, year)
        
        if not thesis_topic:
            raise ValueError("Тема диссертации не может быть пустой")
        if not supervisor:
            raise ValueError("Руководитель не может быть пустым")
        
        self._thesis_topic = thesis_topic
        self._supervisor = supervisor

    @property
    def thesis_topic(self):
        return self._thesis_topic

    @property
    def supervisor(self):
        return self._supervisor

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}, тема диссертации: {self._thesis_topic}"

    def get_status(self):
        return f"Магистрант: {self.name}, тема: {self._thesis_topic}"
