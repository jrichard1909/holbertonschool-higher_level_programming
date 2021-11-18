-- Import the database dump of hbtn_0d_tvshows to your MySQL server: download (same as 10-genre_id_by_show.sql)
-- script that lists all shows contained in the database hbtn_0d_tvshows.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
