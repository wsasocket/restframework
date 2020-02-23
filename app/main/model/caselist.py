from .. import db, flask_bcrypt
import datetime


class CaseList(db.Model):
    """ Case list for todo and complete """
    __tablename__ = "caselist"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    caseHash = db.Column(db.String(64),
                         unique=False,
                         nullable=False,
                         comment='Case Tag')

    caseTitle = db.Column(db.String(256),
                          unique=False,
                          nullable=False,
                          comment='Case Title')

    caseDetail = db.Column(db.Text,
                           unique=False,
                           nullable=False,
                           comment='Case more detail')
    receiveTime = db.Column(db.String(32),
                            nullable=False,
                            comment='Receive Case Time')
    startTime = db.Column(db.String(32),
                          nullable=True,
                          comment='Start To Do Case Time')
    expectTime = db.Column(db.String(32),
                           nullable=False,
                           comment='Expect Complete Case Time')
    completeTime = db.Column(db.String(32),
                             nullable=True,
                             comment='Complete This Case Time')
    usedTime = db.Column(db.Integer,
                         nullable=False,
                         default=0,
                         comment='Hours Used In This Week')
    caseFrom = db.Column(db.String(32),
                         nullable=False,
                         comment='Who Generate the Case')
    caseProject = db.Column(db.String(32),
                            nullable=False,
                            comment='Case belong to Which Project')
    caseStatus = db.Column(db.Integer,
                           nullable=False,
                           default=0,
                           comment='Case Status')
    memo = db.Column(db.String(1024),
                     nullable=True,
                     comment='More Information ')
    userId = db.Column(db.Integer,
                       nullable=False,
                       comment='User id <-> user Table')

    def __repr__(self):
        return "<{} Working Case:'{}'>".format(self.userId, self.caseTitle)
