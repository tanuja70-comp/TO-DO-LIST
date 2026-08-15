BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Tasks" (
	"sno"	INTEGER,
	"title"	TEXT,
	"desc"	TEXT,
	"date_created "	TEXT,
	"status "	TEXT,
	PRIMARY KEY("sno" AUTOINCREMENT)
);
COMMIT;