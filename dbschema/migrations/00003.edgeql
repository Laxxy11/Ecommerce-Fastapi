CREATE MIGRATION m1hz5cxcyrcjo5dfda5o7jbawjmvpaaf2p2ejsap3eennl5jbqp6ma
    ONTO m1t4csdn7nuien6dsa5dnwaiovxps54n2mhin34muucq7mf6f3lxqq
{
  ALTER TYPE default::Product {
      CREATE REQUIRED LINK user: default::User {
          SET REQUIRED USING (<default::User>{});
      };
  };
};
