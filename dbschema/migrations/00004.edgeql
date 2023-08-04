CREATE MIGRATION m1ps7xsvip65wqcujb22yhohbeps6335nse2mdznk4umy7tgld2qya
    ONTO m1hz5cxcyrcjo5dfda5o7jbawjmvpaaf2p2ejsap3eennl5jbqp6ma
{
  ALTER TYPE default::User {
      CREATE REQUIRED PROPERTY role: std::str {
          SET REQUIRED USING (<std::str>{});
          CREATE CONSTRAINT std::exclusive;
      };
  };
};
