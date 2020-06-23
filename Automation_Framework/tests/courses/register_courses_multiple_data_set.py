from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
from ddt import data, ddt, unpack
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "10", "1220", "10", "95123"),("Learn Python 3 from scratch", "10", "1220", "10", "95123"))
    @unpack
    def test_validLogin(self, courseName, ccNum, ccExp, ccCVV, postal):
        self.courses.login("daadkartik@gmail.com", "1234567890")
        self.courses.enterCourseName(courseName)
        self.courses.selectCourseToEnroll(courseName)
        self.courses.enrollCourse(ccNum, ccExp, ccCVV, postal)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment ", result, "Enrollment failed Verification ")
        self.driver.get("https://learn.letskodeit.com/courses")
