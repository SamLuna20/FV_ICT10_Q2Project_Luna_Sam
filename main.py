from pyscript import document, display

def general_weighted_average(e):

    # Get student info
    fname = document.getElementById('fname').value
    sname = document.getElementById('sname').value
    g_s = document.getElementById('g_s').value

    # Get grades
    math = float(document.getElementById('math').value)
    filipino = float(document.getElementById('filipino').value)
    science = float(document.getElementById('science').value)
    ict = float(document.getElementById('ict').value)
    music_arts = float(document.getElementById('m_a').value)
    social_studies = float(document.getElementById('ss').value)

    # Weighted calculation
    weighted_sum = (
        (math * 5) +
        (filipino * 3) +
        (science * 5) +
        (ict * 2) +
        (music_arts * 1) +
        (social_studies * 3)
    )
    total_units = 5 + 3 + 5 + 2 + 1 + 3
    gwa = weighted_sum / total_units

    # get input values (as before)
    subjects = ["Mathematics", "Filipino", "Science", "ICT", "Music & Arts", "Social Studies"]

    summary_text =  f"""
    {subjects[0]}:{math:.0f}
    {subjects[1]}:{filipino:.0f}
    {subjects[2]}:{science:.0f}
    {subjects[3]}:{ict:.0f}
    {subjects[4]}:{music_arts:.0f}
    {subjects[5]}:{social_studies:.0f}
    """
    document.getElementById("grades").classList.remove("d-none")

    # Show results
    display(f'Name: {fname} {sname} — {g_s}', target="student_info")
    display(summary_text, target="summary")
    display(f'Your General Weighted Average is {gwa:.2f}', target="output")

def show(e):
    # access user's club choice
    club = document.getElementById("dropdown").value

    #dictionary of club informations
    name_of_club = {"volleyballvarsity": "Volleyball Varsity", 
                    "gleeclub": "Glee Club", 
                    "scienceclub": "Science Club",
                    "marchingband": "Marching Band",
                    "danceclub": "Dance CLub",
                    "mathclub": "Math Club",
                    "cac": "Communications Arts Club",
                    "cocc": "Cadet Officer Candidate Course",
                    "ssclub": "Social Science Club",
                    "basketballvarsity": "Basketball Varsity"}
    description = {"volleyballvarsity": "This club is made for women who target health, teamwork, and leadership.", 
                   "gleeclub": "This club is fit for those who have voices like an angel!",
                   "scienceclub": "This club is for those who aspire to have Einstein's wit and love for the Earth!",
                   "marchingband": "This club is made for instrument lovers who want to showcase their talent and determination!",
                   "danceclub": "This club is for those who find peace and comfort in dancing!",
                   "mathclub": "This club is for math wizzards who are ready to take on competitions!",
                   "cac": "This club is for those that are creative and literature enthusiasts!",
                   "cocc": "This club is made for those who aspire to serve the country with their hard work!",
                   "ssclub": "This club is for student philosophers who have passion for history!",
                   "basketballvarsity": "This club is for male athletes that enjoy dribbling and hooping!"}
    meeting_time = {"volleyballvarsity": "Wednesday 03:00 - 05:00 PM",
                    "gleeclub": "Monday 03:00- 05:00 PM",
                    "scienceclub": "Tuesday  03:00 - 04:00 PM",
                    "marchingband": "Tuesday and Wednesday 03:00-4:30 PM",
                    "danceclub": "Tuesday 03:00 - 05:00 PM",
                    "mathclub": "Monday 02:30- 03:00 PM",
                    "cac": "Wednesday 03:00 - 04:00 PM, Friday 03:00 - 04:00 PM",
                    "cocc": "Wednesday 02:30 -04:30 PM",
                    "ssclub": "Tuesday 03:00 - 4:00 PM",
                    "basketballvarsity": "Monday 03:00 - 04:00 PM"}
    location = {"volleyballvarsity": "Quadrangle",
                "gleeclub": "High School Music Room",
                "scienceclub": "Room 404",
                "marchingband": "Band Room",
                "danceclub": "Teatro Preciosa",
                "mathclub": "Room 404",
                "cac": "Room 406",
                "cocc": "Quadrangle/ Teatro Preciosa",
                "ssclub": "Room 409",
                "basketballvarsity": "Quadrangle"}
    advisor = {"volleyballvarsity": "Mr. Adrian Ruiz",
                "gleeclub": "Mr. Denver Martin",
                "scienceclub": "Ms. Jameelyn Maramag",
                "marchingband": "Mr. Emilio Alumno",
                "danceclub": "Mr. Alfred Cases",
                "mathclub": "Mr. Nicole Gabuya",
                "cac": "Ms. Yannis Fernandez",
                "cocc": "SSgt. Jemima David PA (Res)",
                "ssclub": "Mr. Roberto Lim",
                "basketballvarsity": "Mr. Adrian Ruiz"}
    number_of_members = {"volleyballvarsity": "23",
                "gleeclub": "20",
                "scienceclub": "20",
                "marchingband": "15",
                "danceclub": "28",
                "mathclub": "20",
                "cac": "17",
                "cocc": "22",
                "ssclub": "20",
                "basketballvarsity": "16"}
    category = {"volleyballvarsity": "Non-academic",
                "gleeclub": "Non-academic",
                "scienceclub": "Academic",
                "marchingband": "Non-Academic",
                "danceclub": "Non-academic",
                "mathclub": "Academic",
                "cac": "Academic",
                "cocc": "Non-academic",
                "ssclub": "Academic",
                "basketballvarsity": "Non-academic"}
    #display club info after button is clicked
    document.getElementById("clubinfo").classList.remove("d-none")

    #display club info
    display(name_of_club[club],target="name")
    display(description[club],target="description")
    display(meeting_time[club],target="meetingtime")
    display(location[club],target="location")
    display(advisor[club],target="advisor")
    display(number_of_members[club],target="numofmembers")
    display(category[club],target="category")