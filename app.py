import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from lr_prediction import pred

db_username = os.environ['DB_USERNAME']
db_password = os.environ['DB_PASSWORD']
db_name = os.environ['DB_NAME']
db_host = os.environ['DB_HOST']
db_port = os.environ['DB_PORT']
db_uri = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
print(f"Connecting db @{db_uri}")
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy()
db.init_app(app)
class Team(db.Model):
    __tablename__ = "teams"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.Integer, nullable=False)
    obp = db.Column(db.Float, nullable=False)
    slg = db.Column(db.Float, nullable=False)
    ba = db.Column(db.Float, nullable=False)
    g = db.Column(db.Integer, nullable=False)
    oobp = db.Column(db.Float, nullable=False)
    oslg = db.Column(db.Float, nullable=False)
    league_nl = db.Column(db.Boolean, nullable=False)
    playoffs_1  = db.Column(db.Boolean, nullable=False)
    rd = db.Column(db.Float, nullable=True)
    def __init__(self, Year, OBP, SLG, BA, G, OOBP, OSLG, League_NL, Playoffs_1, RD):
        self.year = Year
        self.obp = OBP
        self.slg = SLG
        self.ba = BA
        self.g = G
        self.oobp = OOBP
        self.oslg = OSLG
        self.league_nl = League_NL
        self.playoffs_1 = Playoffs_1
        self.rd = RD

@app.route("/")
def home():
    return "Hello from my Containerized Server"

@app.route('/teams', methods=['POST'])
def add_team():
    request_data = request.get_json()
    request_data['RD'] = pred(request_data)
    new_team = Team( Year= request_data['Year'],
                     OBP=request_data['OBP'],
                     SLG=request_data['SLG'],
                     BA=request_data['BA'],
                     G=request_data['G'],
                     OOBP=request_data['OOBP'],
                     OSLG=request_data['OSLG'],
                     League_NL=request_data['League_NL'],
                     Playoffs_1=request_data['Playoffs_1'],
                     RD = request_data['RD'])
    db.session.add(new_team)
    db.session.commit()
    return "Team added successfully"

@app.route('/teams')
def show_teams():
    teams = Team.query.all()
    team_list = {}
    for team in teams:
        team_list[team.id] = {
            'Year': team.year,
            'OBP': team.obp,
            'SLG': team.slg,
            'BA': team.ba,
            'G': team.g,
            'OOBP': team.oobp,
            'OSLG': team.oslg,
            'League_NL': team.league_nl,
            'Playoffs_1': team.playoffs_1,
            'RD': team.rd
        }
    return team_list

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555)