class Applicant:
    def __init__(self, name, identification):
        self.name = name
        self.identification = identification
        self.application = None

    def submit_application(self, application):
        self.application = application


class JobApplication:
    def __init__(self, identification, name):
        self.identification = identification
        self.name = name
        self.applicants = []
        self.opening = []


    def add_applicant(self, applicant):
        self.applicants.append(applicant)
        applicant.application = self

class Interview:
    def __init__(self, name, interviewdate):
        self.name = name
        self.date = interviewdate
        self.manager = []

    def schedule_interview(self, manager):
        self.manager.append(manager)

class JobOffering:
    def __init__(self, job_id, job_name, job_date, job_requirements, job_description, job_offering_status):
        self.job_id = job_id
        self.job_name = job_name
        self.job_date = job_date
        self.job_requirements = job_requirements
        self.job_description = job_description
        self.job_offering_status = job_offering_status
        self.applications = []


class Manager:
    def __init__(self, manager_id, manager_firstname, manager_lastname):
        self.manager_id = manager_id
        self.manager_firstname = manager_firstname
        self.manager_lastname = manager_lastname
        self.job_offering = ""

    def post_job_offering(self, job_offering):
        self.job_offering = job_offering

    def edit_job_offering(self, job_offering):
        self.job_offering = job_offering


class Employee:
    def __init__(self, employee_id, employee_firstname, employee_lastname):
        self.employee_id = employee_id
        self.employee_firstname = employee_firstname
        self.employee_lastname = employee_lastname
        self.availabilities = []

    def fill(self, fill_availability):
        self.availabilities.append(fill_availability)
        fill_availability.add_employee(self)


class Availability:
    def __init__(self, availability_id, availability_date):
        self.availability_id = availability_id
        self.availability_date = availability_date
        self.employee = []

    def add_employee(self, thisday):
        self.employee.append(Schedule(self, thisday))
        return self.employee[-1]


class Schedule:
    def __init__(self, schedule_id, schedule_date):
        self.schedule_id = schedule_id
        self.schedule_date = schedule_date
        self.employee = []


Monday = Availability("162_2023", "June 11")
Tuesday = Availability("163_2023", "June 12")
Wednesday = Availability("164_2023", "June 13")
Thursday = Availability("165_2023", "June 14")
Friday = Availability("166_2023", "June 15")
Saturday = Availability("167_2023", "June 16")
Sunday = Availability("168_2023", "June 17")


Jack = Employee("1", "Jack", "Jefferson")
Joe = Employee("2", "Joe", "Jackson")
Jerry = Employee("3", "Jerry", "Joseph")
Joey = Employee("4", "Joey", "James")
Jeremy = Employee("5", "Jeremy", "Jeremiahs")

Jack.fill(Monday)
Jack.fill(Saturday)

Joe.fill(Tuesday)
Joe.fill(Friday)

Jerry.fill(Wednesday)
Jerry.fill(Saturday)

Joey.fill(Thursday)
Joey.fill(Sunday)

Jeremy.fill(Saturday)
Jeremy.fill(Sunday)

schedule = {
    "June 11": [],
    "June 12": [],
    "June 13": [],
    "June 14": [],
    "June 15": [],
    "June 16": [],
    "June 17": [],
}

for employee in [Jack, Joe, Jerry, Joey, Jeremy]:
    for availability in employee.availabilities:
        if availability.availability_date in schedule:
            schedule[availability.availability_date].append(employee.employee_firstname + " " + employee.employee_lastname)

for date, employees in schedule.items():
    print(date + ": " + ", ".join(employees))



job1 = JobOffering("JOB01", "Server", "2023-06-01", "1 year of experience in customer service", "We are seeking a server to join our restaurant team", "open")
job2 = JobOffering("JOB02", "Bartender", "2023-06-02", "1 year of experience in bartending", "We are seeking a bartender to join our restaurant team", "open")
job3 = JobOffering("JOB03", "Chef", "2023-06-03", "5 years of experience in a restaurant", "We are seeking a chef to join our restaurant team", "open")

app1_job1 = JobApplication("APP01", "Server Job Application")
app1_job1.add_applicant(Applicant("John", "12345"))
app1_job1.add_applicant(Applicant("Jane", "67890"))

app2_job2 = JobApplication("APP02", "Bartender Job Application")
app2_job2.add_applicant(Applicant("Bob", "11111"))
app2_job2.add_applicant(Applicant("Mary", "22222"))

app3_job3 = JobApplication("APP03", "Chef Job Application")
app3_job3.add_applicant(Applicant("Alice", "33333"))

job1.applications = [app1_job1]
job2.applications = [app2_job2]
job3.applications = [app3_job3]

for job in [job1, job2, job3]:
    print("Job Offering: " + job.job_name)
    print("Job Requirements: " + job.job_requirements)
    print("Job Description: " + job.job_description)
    print("Job Status: " + job.job_offering_status)
    print("Applications:")
    for app in job.applications:
        print("  Job Application: " + app.name)
        for applicant in app.applicants:
            print("    Applicant: " + applicant.name)
    print()

