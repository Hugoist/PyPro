from ninja import Schema


# STUDENT
class StudentCreateSchema(Schema):
    first_name: str
    last_name: str
    email: str


class StudentReadSchema(Schema):
    id: int
    first_name: str
    last_name: str
    email: str


# COURSE
class CourseCreateSchema(Schema):
    title: str
    description: str | None = None


class CourseReadSchema(Schema):
    id: int
    title: str
    description: str | None = None
    average_score: float | None


# ENROLLMENT
class EnrollmentCreateSchema(Schema):
    student_id: int
    course_id: int


class EnrollmentReadSchema(Schema):
    id: int
    student_id: int
    course_id: int


# EXAM RESULT
class ExamResultCreateSchema(Schema):
    student_id: int
    course_id: int
    score: int  # можно ограничить 0–100 через валидацию Ninja


class ExamResultReadSchema(Schema):
    id: int
    student_id: int
    course_id: int
    score: int
