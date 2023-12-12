-- Inserting data into Movie
INSERT INTO Movie (name, genre, release_date, director, duration_minutes) VALUES
('Inception', 'Sci-Fi', '2010-07-16', 'Christopher Nolan', 148),
('The Shawshank Redemption', 'Drama', '1994-09-23', 'Frank Darabont', 142),
('The Dark Knight', 'Action', '2008-07-18', 'Christopher Nolan', 152),
('Pulp Fiction', 'Crime', '1994-10-14', 'Quentin Tarantino', 154),
('Forrest Gump', 'Drama', '1994-07-06', 'Robert Zemeckis', 142),
('The Godfather', 'Crime', '1972-03-24', 'Francis Ford Coppola', 175),
('The Matrix', 'Action', '1999-03-31', 'The Wachowskis', 136),
('Schindler''s List', 'Biography', '1993-11-30', 'Steven Spielberg', 195),
('Fight Club', 'Drama', '1999-10-15', 'David Fincher', 139),
('Inglourious Basterds', 'Adventure', '2009-08-21', 'Quentin Tarantino', 153);

-- Inserting data into BoxOffice
INSERT INTO BoxOffice (total_gross, opening_weekend, movie_id) VALUES
(829895144, 62785337, 1),
(289317794, 7273270, 2),
(1004558444, 158411483, 3),
(213928762, 93000, 4),
(678226205, 24717811, 5),
(246120986, 3023932, 6),
(465343787, 27788348, 7),
(322208889, 6566364, 8),
(100851705, 11045010, 9),
(321455689, 38403780, 10);

-- Inserting data into Review
INSERT INTO Review (review_text, rating, visit_date, user_id, movie_id) VALUES
('Mind-bending plot!', 4.5, '2023-11-15', 1, 1),
('A masterpiece.', 4.7, '2023-11-20', 2, 2),
('Thrilling action!', 4.9, '2023-10-05', 4, 3),
('Cinematic excellence.', 4.6, '2023-10-10', 3, 4),
('Heartwarming story.', 4.8, '2023-10-25', 5, 5),
('Twists and turns.', 4.4, '2023-10-30', 6, 6),
('Captivating performances.', 4.3, '2023-11-01', 7, 7),
('Emotional journey.', 4.5, '2023-11-05', 8, 8),
('Thought-provoking.', 4.2, '2023-11-10', 9, 9),
('Quentin brilliance.', 4.7, '2023-11-20', 10, 10);

-- Inserting data into Description
INSERT INTO Description (plot, tagline, poster_url, movie_id) VALUES
('A heist thriller with a twist in reality.', 'Your mind is the scene of the crime.', 'inception_poster.jpg', 1),
('Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.', 'Fear can hold you prisoner. Hope can set you free.', 'shawshank_redemption_poster.jpg', 2),
('A vigilante known as Batman sets out to dismantle the remaining criminal organizations that plague the city.', 'Why So Serious?', 'dark_knight_poster.jpg', 3),
('The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.', 'Girls like me don''t make invitations like this to just anyone!', 'pulp_fiction_poster.jpg', 4),
('The presidencies of Kennedy and Johnson, the events of Vietnam, Watergate, and other historical events unfold through the perspective of an Alabama man with an IQ of 75.', 'Life is like a box of chocolates...', 'forrest_gump_poster.jpg', 5),
('The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.', 'An offer you can''t refuse.', 'godfather_poster.jpg', 6),
('A computer hacker learns about the true nature of his reality and his role in the war against its controllers.', 'Reality is a thing of the past.', 'matrix_poster.jpg', 7),
('In German-occupied Poland during World War II, Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazis.', 'Whoever saves one life, saves the world entire.', 'schindlers_list_poster.jpg', 8),
('An insomniac office worker and a devil-may-care soapmaker form an underground fight club that evolves into an anarchistic organization.', 'How much can you know about yourself if you''ve never been in a fight?', 'fight_club_poster.jpg', 9),
('In Nazi-occupied France during World War II, a plan to assassinate Nazi leaders by a group of Jewish U.S. soldiers coincides with a theater owner''s vengeful plans for the same.', 'Once upon a time in Nazi-occupied France...', 'inglourious_basterds_poster.jpg', 10);

-- Inserting data into Actor
INSERT INTO Actor (name) VALUES
('Leonardo DiCaprio'),
('Tim Robbins'),
('Christian Bale'),
('John Travolta'),
('Tom Hanks'),
('Marlon Brando'),
('Keanu Reeves'),
('Liam Neeson'),
('Edward Norton'),
('Brad Pitt');

-- Inserting data into MovieActors
INSERT INTO MovieActors (Actor_actor_id, Movie_movie_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10);

-- Inserting data into Rating
INSERT INTO Rating (user_id, rating_value, movie_id) VALUES
('1', 4.5, 1),
('2', 4.7, 2),
('4', 4.9, 3),
('3', 4.6, 4),
('5', 4.8, 5),
('6', 4.4, 6),
('7', 4.3, 7),
('8', 4.5, 8),
('9', 4.2, 9),
('10', 4.7, 10);

-- Inserting data into Fact
INSERT INTO Fact (fact_text, movie_id) VALUES
('Inception was filmed in six countries.', 1),
('The Shawshank Redemption is based on a Stephen King novella.', 2),
('Heath Ledger won an Oscar for his role as the Joker.', 3),
('Pulp Fiction was Quentin Tarantino''s second film.', 4),
('Tom Hanks won an Oscar for his role in Forrest Gump.', 5),
('The Godfather is based on a novel of the same name.', 6),
('Keanu Reeves performed many of his own stunts in The Matrix.', 7),
('Schindler''s List won seven Academy Awards.', 8),
('Fight Club is based on a novel by Chuck Palahniuk.', 9),
('Inglourious Basterds features multiple languages, including English, French, German, and Italian.', 10);
