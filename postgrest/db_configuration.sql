create schema api;

create table api.todos (
  id int primary key generated by default as identity,
  done boolean not null default false,
  task text not null,
  due timestamptz
);

insert into api.todos (task) values
  ('finish tutorial 0'), ('pat self on back');

create role web_anon nologin;

grant usage on schema api to web_anon;
grant select on api.todos to web_anon;

-- It’s a good practice to create a dedicated role for connecting to the database, 
-- instead of using the highly privileged postgres role. So we’ll do that, name the role authenticator
-- and also grant it the ability to switch to the web_anon role

create role authenticator noinherit login password 'mysecretpassword';
grant web_anon to authenticator;
