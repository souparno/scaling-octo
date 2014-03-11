drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title text not null,
  text text not null
);
drop table if exists resume;
create table resume (
 id integer,
 email string,
 name string,
 address text,
 contact_number string,
 mobile_number string,
 dob date,
 experience_years integer,
 experience_months integer,
 title text,
 current_location integer,
 preferred_location integer,
 current_employer integer,
 current_designation integer,
 salary integer,
 ug_course integer,
 pg_course integer,
 ppg_course integer
);
