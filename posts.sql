DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    titolo TEXT, 
    info TEXT,
    descrizione TEXT
);

INSERT INTO posts (titolo, info, descrizione) VALUES (
    'Benvenuti in Hazen Tech',
    'IL SEGUENTE PARAGRAFO  IN TEST',
    'Eccoci qui, è arrivato il giorno del 11 giugno del 2022, la rinascita di HazenTech'

);
