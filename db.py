import psycopg2
import bcrypt
import os
from dotenv import load_dotenv

load_dotenv()

def get_users():

    connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
    )

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users;")

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    return rows


def get_user(user_id):

    connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT name, email, goal_name
        FROM users
        JOIN goals
        ON users.goal_id = goals.goal_id
        WHERE user_id = %s;
        """,
        (user_id,)
    )

    user = cursor.fetchone()

    cursor.close()
    connection.close()

    return user


def get_user_skills(user_id):

    connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
    )
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT skill_name
        FROM skills
        JOIN user_skills
        ON skills.skill_id = user_skills.skill_id
        WHERE user_skills.user_id = %s;
        """,
        (user_id,)
    )

    skills = cursor.fetchall()

    cursor.close()
    connection.close()

    return skills


def get_missing_skills(user_id):

    connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT skills.skill_id, skills.skill_name, skills.reason
        FROM skills
        JOIN goal_skills
        ON skills.skill_id = goal_skills.skill_id

        WHERE goal_id = (

            SELECT goal_id
            FROM users
            WHERE user_id = %s

        )

        AND skills.skill_id NOT IN (

            SELECT skill_id
            FROM user_skills
            WHERE user_id = %s

        );
        """,
        (user_id, user_id)
    )

    missing_skills = cursor.fetchall()

    cursor.close()
    connection.close()

    return missing_skills


def get_progress(user_id):

    connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
    )

    cursor = connection.cursor()

    # Current Skills
    cursor.execute(
    """
    SELECT COUNT(*)
    FROM user_skills
    JOIN goal_skills
    ON user_skills.skill_id = goal_skills.skill_id
    WHERE user_id = %s
    AND goal_id = (
        SELECT goal_id
        FROM users
        WHERE user_id = %s
    );
    """,
    (user_id, user_id)
    )

    current_skills = cursor.fetchone()[0]

    # Total Goal Skills
    cursor.execute(
    """
    SELECT COUNT(*)
    FROM goal_skills
    WHERE goal_id = (
        SELECT goal_id
        FROM users
        WHERE user_id = %s
    );
    """,
    (user_id,)
    )
    total_skills = cursor.fetchone()[0]

    progress = (current_skills / total_skills) * 100

    cursor.close()
    connection.close()

    return current_skills, total_skills, round(progress, 2)


def add_user_skill(user_id, skill_id):

    connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
    )
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO user_skills (user_id, skill_id)
        VALUES (%s, %s);
        """,
        (user_id, skill_id)
    )

    connection.commit()

    cursor.close()
    connection.close()

def get_next_skill(user_id):

    missing_skills = get_missing_skills(user_id)

    if not missing_skills:
        return None, None

    next_skill = missing_skills[0]

    skill_name = next_skill[1]
    reason = next_skill[2]

    return skill_name, reason

def create_user(name, email, password, goal_id):

    connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
    )

    cursor = connection.cursor()
    hashed_password = bcrypt.hashpw(
    password.encode("utf-8"),
    bcrypt.gensalt()
    ).decode("utf-8")

    cursor.execute(
        """
        INSERT INTO users (name, email, hashed_password, goal_id)
        VALUES (%s, %s, %s ,%s);
        """,
        (name, email, hashed_password , goal_id)
    )

    connection.commit()

    cursor.close()
    connection.close()

def login_user(email, password):

    connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
    )
    

    cursor = connection.cursor()

    cursor.execute(
    '''
    SELECT user_id, name, email, hashed_password, goal_id
    FROM users
    WHERE email = %s;
    ''',
    (email,)
    )

    user = cursor.fetchone()
    if user and bcrypt.checkpw(
    password.encode("utf-8"),
    user[3].encode("utf-8")
    ):
        user = (user[0], user[1], user[2], user[4])
    else:
        user = None

    cursor.close()
    connection.close()

    return user

def get_goals():

    connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT goal_id, goal_name
        FROM goals;
        """
    )

    goals = cursor.fetchall()

    cursor.close()
    connection.close()

    return goals

def get_skills():

    connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
    )
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT skill_id, skill_name
        FROM skills;
        """
    )

    skills = cursor.fetchall()

    cursor.close()
    connection.close()

    return skills

def email_exists(email):

    connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT user_id
        FROM users
        WHERE email = %s;
        """,
        (email,)
    )

    user = cursor.fetchone()

    cursor.close()
    connection.close()

    return user is not None