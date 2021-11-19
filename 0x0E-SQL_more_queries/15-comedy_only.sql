-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 14-my_genres.sql)
-- script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT tv_shows.title
FROM (tv_genres
INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id)
INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title;
