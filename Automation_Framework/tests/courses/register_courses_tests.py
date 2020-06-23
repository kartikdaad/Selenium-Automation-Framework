from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_validLogin(self):
        self.courses.login("daadkartik@gmail.com", "1234567890")
        self.courses.enterCourseName("Javascript")
        self.courses.selectCourseToEnroll("JavaScript for beginners")
        self.courses.enrollCourse("6074 3100 9055 1780", "0223", "456", "90412")
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment ", result, "Enrollment failed Verification ")
