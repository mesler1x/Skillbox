import sqlite3

conn = sqlite3.connect('task1.sqlite')
c = conn.cursor()

c.execute('''CREATE TABLE actors
             (actor_id INTEGER PRIMARY KEY AUTOINCREMENT,
              actor_name TEXT)''')

c.execute('''CREATE TABLE movies
             (movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
              movie_title TEXT)''')

c.execute('''CREATE TABLE actor_movie
             (actor_id INT,
              movie_id INT,
              PRIMARY KEY (actor_id, movie_id),
              FOREIGN KEY (actor_id) REFERENCES actors (actor_id),
              FOREIGN KEY (movie_id) REFERENCES movies (movie_id))''')
conn_netflix = sqlite3.connect('netflix.sqlite')
c_netflix = conn_netflix.cursor()
c_netflix.execute('''ALTER TABLE netflix_title
    DROP COLUMN type,
    DROP COLUMN director,
    DROP COLUMN country,
     DROP COLUMN added,
     DROP COLUMN release_year,
     DROP COLUMN rating,
     DROP COLUMN duration,
     DROP COLUMN listed_in''')
data = c_netflix.execute('''SELECT * FROM netflix_titles''')

for row in data:
    show_id, title, cast = row
    movie_id = c.execute('INSERT INTO movies (movie_title) VALUES (?)', (title,)).lastrowid
    actors = cast.split(', ')
    for actor in actors:
        actor_id = c.execute('INSERT INTO actors (actor_name) VALUES (?)', (actor,)).lastrowid
        c.execute('INSERT INTO actor_movie (actor_id, movie_id) VALUES (?, ?)', (actor_id, movie_id))

conn.commit()
conn.close()

c.execute('''SELECT a1.actor_name, a2.actor_name, COUNT(*) as count
             FROM actor_movie am1
             JOIN actors a1 ON am1.actor_id = a1.actor_id
             JOIN actor_movie am2 ON am1.movie_id = am2.movie_id
             JOIN actors a2 ON am2.actor_id = a2.actor_id
             WHERE a1.actor_name <> a2.actor_name
             GROUP BY a1.actor_name, a2.actor_name
             ORDER BY count DESC
             LIMIT 1''')

result = c.fetchone()
if result:
    actor1, actor2, count = result
    print(
        f"Наиболее встречающиеся пары это {actor1} и {actor2}, они работали вместе в {count} фильмах.")
else:
    print("Нет найденых пар.")
