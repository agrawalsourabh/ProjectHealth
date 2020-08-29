from project import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class UserLogin(db.Model, UserMixin):
    empId = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, empId, password):
        self.empId = empId
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class User(db.Model):
    userEmpId = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    userName = db.Column(db.String(20),  nullable=False)
    userTitle = db.Column(db.String(5),  nullable=False)
    userCompanyStartDate = db.Column(db.DateTime,  nullable=False)
    userCompanyEndDate = db.Column(db.DateTime,  nullable=False)
    userSupervisor = db.Column(db.String(20),  nullable=False)
    userEmailID = db.Column(db.String(120), unique=True, nullable=False)
    userOnsite = db.Column(db.String(20),  nullable=False)
    userLocation = db.Column(db.String(20),  nullable=False)
    userVisaAvailable = db.Column(db.String(2),  nullable=False)
    assignSystemRole = db.Column(db.String(20),  nullable=False)

    project = db.relationship('Project', backref='user', lazy=True)

    def __init__(self, userEmpId, userName, userTitle, userCompanyStartDate, userCompanyEndDate, userSupervisor, userEmailID,
                userOnsite, userLocation, userVisaAvailable, assignSystemRole):
                self.userEmailID = userEmailID
                self.userEmpId = userEmpId
                self.userName = userName
                self.userTitle = userTitle
                self.userCompanyStartDate = userCompanyStartDate
                self.userCompanyEndDate = userCompanyEndDate
                self.userSupervisor = userSupervisor
                self.userOnsite = userOnsite
                self.userLocation = userLocation
                self.userVisaAvailable = userVisaAvailable
                self.assignSystemRole = assignSystemRole


class Client(db.Model):
    clientName = db.Column(db.String(20), unique=True, nullable=False)
    clientId = db.Column(db.String(20),  nullable=False, primary_key=True)
    clientStartDate = db.Column(db.DateTime,  nullable=False)
    clientEndDate = db.Column(db.DateTime,  nullable=False)
    projectId = db.Column(db.String(120),  nullable=False)


    def __init__(self, clientName, clientId, clientStartDate, clientEndDate, projectId):
        self.clientName = clientName
        self.clientId = clientId
        self.clientStartDate = clientStartDate
        self.clientEndDate = clientEndDate
        self.projectId = projectId


class Project(db.Model):
    projectName = db.Column(db.String(20) )
    projectId = db.Column(db.String(20), unique=True, nullable=False, primary_key=True)
    projectStartDate = db.Column(db.DateTime,  nullable=False)
    projectEndDate = db.Column(db.DateTime,  nullable=False)
    projectSponsor = db.Column(db.String(20),  nullable=False)
    userEmpId = db.Column(db.String(20), db.ForeignKey('user.userEmpId'))
    projectManager = db.Column(db.String(20),  nullable=False)
    milestoneName = db.Column(db.String(30),  nullable=False)
    milestoneStartDate = db.Column(db.DateTime,  nullable=False)
    milestoneEndDate = db.Column(db.DateTime,  nullable=False)
    milestoneComments = db.Column(db.String(120),  nullable=False)
    milestoneStatus = db.Column(db.String(120))

    def __init__(self, projectName, projectId, projectStartDate, projectEndDate, projectSponsor, userEmpId, 
                projectManager, milestoneName, milestoneStartDate, milestoneEndDate, milestoneComments, milestoneStatus):
                self.projectName = projectName
                self.projectId = projectId
                self.projectStartDate = projectStartDate
                self.projectEndDate = projectEndDate
                self.projectSponsor = projectSponsor
                self.userEmpId = userEmpId
                self.projectManager = projectManager
                self.milestoneName = milestoneName
                self.milestoneStartDate = milestoneStartDate
                self.milestoneEndDate = milestoneEndDate
                self.milestoneComments = milestoneComments
                self.milestoneStatus = milestoneStatus


class WSRUpdates(db.Model):
    projectId =  db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    activitiesCompleted =  db.Column(db.String(80))
    activitiesCompletedStatus = db.Column(db.DateTime)
    activitiesPlanned = db.Column(db.String(80))
    activitiesPlannedStatus = db.Column(db.DateTime)
    updatesComments = db.Column(db.String(80))
    risks = db.Column(db.String(80)) 
    riskProbabilitySeverity =db.Column(db.String(80))
    riskMitigation = db.Column(db.String(80))
    achievements = db.Column(db.String(80))


    def __init__(self, projectId, activitiesCompleted, activitiesCompletedStatus, activitiesPlanned, activitiesPlannedStatus,
                updatesComments, risks, riskProbabilitySeverity, riskMitigation, achievements):
                self.projectId = projectId
                self.activitiesCompleted = activitiesCompleted
                self.activitiesCompletedStatus = activitiesCompletedStatus
                self.activitiesPlanned = activitiesPlanned
                self.activitiesPlannedStatus = activitiesPlannedStatus
                self.updatesComments = updatesComments
                self.risks = risks
                self.riskProbabilitySeverity = riskProbabilitySeverity
                self.riskMitigation = riskMitigation
                self.achievements = achievements


class ProjectMapping(db.Model):
    projectID = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    projectName = db.Column(db.String(80))
    userProjectStartDate = db.Column(db.String(80))
    userProjectEndDate = db.Column(db.String(80))
    billableYesNo = db.Column(db.String(80))
    billableStartDate = db.Column(db.String(80))
    billableEndDate =db.Column(db.String(80))
    allocationPercentage = db.Column(db.String(80))

    def __init__(self, projectID, projectName, userProjectStartDate, userProjectEndDate, billableYesNo, 
                billableStartDate, billableEndDate, allocationPercentage):
                self.projectID = projectID
                self.projectName = projectName
                self.userProjectStartDate = userProjectStartDate
                self.userProjectEndDate = userProjectEndDate
                self.billableYesNo = billableYesNo
                self.billableStartDate = billableStartDate
                self.billableEndDate = billableEndDate
                self.allocationPercentage = allocationPercentage




