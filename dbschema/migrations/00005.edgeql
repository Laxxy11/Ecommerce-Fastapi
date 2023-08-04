CREATE MIGRATION m1llex6izoxwzbrwvmqxg64wnpzuobjzhttbivldospbhqhjcdh73a
    ONTO m1ps7xsvip65wqcujb22yhohbeps6335nse2mdznk4umy7tgld2qya
{
  ALTER TYPE default::User {
      ALTER PROPERTY role {
          RENAME TO user_role;
      };
  };
};
