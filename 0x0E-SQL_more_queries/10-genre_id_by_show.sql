--Script that lists all showss in hbtn_0d_tvshows which has atleast one genre linked
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
JOIN tv_show_genres ON tv_show.id = tv_show_genres.show_id
ORDER BY tv_show.title, tv_show_genres.genre_id;
