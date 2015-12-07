SELECT * FROM Meetups WHERE Start > "2015.11.27";
SELECT Name, Introduction FROM Users WHERE Introduction IS NULL ;
# SELECT * FROM Meetups INNER JOIN Statuses ON Meetups.Id = Statuses.Id INNER JOIN Users ON Statuses.Id = Users.Id WHERE Users.Name = "Person Two";