from django.shortcuts import get_object_or_404
from ninja import Router

from app.api.auth import auth
from app.models.student_course import Student, Course, Enrollment, ExamResult
from app.schemas.student_course import (
    StudentCreateSchema, StudentReadSchema,
    CourseCreateSchema, CourseReadSchema,
    EnrollmentCreateSchema, EnrollmentReadSchema,
    ExamResultCreateSchema, ExamResultReadSchema,
)

router = Router(tags=["StudentCourse"])


# STUDENTS

@router.post("/students", auth=auth, response=StudentReadSchema)
def create_student(request, payload: StudentCreateSchema):
    student = Student.objects.create(**payload.dict())
    return student


@router.get("/students", response=list[StudentReadSchema])
def list_students(request):
    return Student.objects.all()


@router.get("/students/{student_id}", response=StudentReadSchema)
def get_student(request, student_id: int):
    return get_object_or_404(Student, id=student_id)


@router.delete("/students/{student_id}", auth=auth)
def delete_student(request, student_id: int):
    get_object_or_404(Student, id=student_id).delete()
    return {"success": True}


# COURSES

@router.post("/courses", auth=auth, response=CourseReadSchema)
def create_course(request, payload: CourseCreateSchema):
    course = Course.objects.create(**payload.dict())
    return course


@router.get("/courses", response=list[CourseReadSchema])
def list_courses(request):
    return Course.objects.all()


@router.get("/courses/{course_id}", response=CourseReadSchema)
def get_course(request, course_id: int):
    return get_object_or_404(Course, id=course_id)


@router.delete("/courses/{course_id}", auth=auth)
def delete_course(request, course_id: int):
    get_object_or_404(Course, id=course_id).delete()
    return {"success": True}


# ENROLL STUDENTS

@router.post("/enroll", auth=auth, response=EnrollmentReadSchema)
def enroll_student(request, payload: EnrollmentCreateSchema):
    student = get_object_or_404(Student, id=payload.student_id)
    course = get_object_or_404(Course, id=payload.course_id)

    enrollment, _ = Enrollment.objects.get_or_create(student=student, course=course)
    return enrollment


@router.delete("/enroll", auth=auth)
def unenroll_student(request, payload: EnrollmentCreateSchema):
    enrollment = Enrollment.objects.filter(
        student_id=payload.student_id,
        course_id=payload.course_id
    ).first()

    if not enrollment:
        return {"success": False, "message": "Student is not enrolled in this course"}

    enrollment.delete()
    return {"success": True}


@router.get("/enrollments", response=list[EnrollmentReadSchema])
def list_enrollments(request):
    return Enrollment.objects.all()


# EXAM RESULTS

@router.post("/exam", auth=auth, response=ExamResultReadSchema)
def set_exam_result(request, payload: ExamResultCreateSchema):
    student = get_object_or_404(Student, id=payload.student_id)
    course = get_object_or_404(Course, id=payload.course_id)

    result, _ = ExamResult.objects.update_or_create(
        student=student,
        course=course,
        defaults={"score": payload.score}
    )
    return result


@router.get("/exam", response=list[ExamResultReadSchema])
def list_results(request):
    return ExamResult.objects.all()
