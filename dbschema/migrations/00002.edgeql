CREATE MIGRATION m1t4csdn7nuien6dsa5dnwaiovxps54n2mhin34muucq7mf6f3lxqq
    ONTO m1hwspkehry77fqzrh3irsn4ckf2ivgbi42ozv3brumi6jgoafvfuq
{
  CREATE TYPE default::Category {
      CREATE REQUIRED PROPERTY name: std::str {
          CREATE CONSTRAINT std::exclusive;
      };
  };
  CREATE TYPE default::Product {
      CREATE MULTI LINK categories: default::Category;
      CREATE PROPERTY created_at: std::datetime {
          SET default := (std::datetime_current());
          SET readonly := true;
      };
      CREATE PROPERTY description: std::str;
      CREATE REQUIRED PROPERTY price: std::float64;
      CREATE REQUIRED PROPERTY title: std::str {
          CREATE CONSTRAINT std::exclusive;
      };
      CREATE PROPERTY updated_at: std::datetime {
          SET default := (std::datetime_current());
          SET readonly := true;
      };
  };
};
