from ninja import Router
from .auth import auth_router
from .tasks import router as tasks_router
from .ecommerce import router as ecommerce_router
from .imdb import router as imdb_router
from .blog import router as blog_router
from .monitoring import router as monitoring_router
from .library import router as library_router
from .student_course import router as students_course_router

router = Router()

router.add_router("/auth", auth_router, tags=["Auth"])
router.add_router("/tasks", tasks_router, tags=["Tasks"])
router.add_router("/ecommerce", ecommerce_router, tags=["Ecommerce"])
router.add_router("/imdb", imdb_router, tags=["IMDb"])
router.add_router("/blog", blog_router, tags=["Blog"])
router.add_router("/monitoring", monitoring_router, tags=["Monitoring"])
router.add_router("/library", library_router, tags=["Library"])
router.add_router("/students_course", students_course_router, tags=["StudentCourse"])
