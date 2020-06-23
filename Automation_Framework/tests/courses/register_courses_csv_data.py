from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
from ddt import data, ddt, unpack
from utilities.read_data import getCSVData
from pages.home.navigation_page import NavigationPage
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.navigateToAllCourses()

    @pytest.mark.run(order=1)
    @data(*getCSVData("/C:/Users/Lenovo/workspace_python/Automation_Framework"))
    @unpack
    def test_validLogin(self, courseName, ccNum, ccExp, ccCVV, postal):
        self.courses.login("daadkartik@gmail.com", "1234567890")
        self.courses.enterCourseName(courseName)
        self.courses.selectCourseToEnroll(courseName)
        self.courses.enrollCourse(ccNum, ccExp, ccCVV, postal)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment ", result, "Enrollment failed Verification ")
