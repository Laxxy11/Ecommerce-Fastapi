CREATE MIGRATION m1xioeotlhcwftk34y6s2s3xepuhclwd3tvnmxmhik3ux7xotk3xvq
    ONTO m1llex6izoxwzbrwvmqxg64wnpzuobjzhttbivldospbhqhjcdh73a
{
  CREATE TYPE default::Cart {
      CREATE MULTI LINK products: default::Product;
      CREATE REQUIRED LINK user: default::User;
      CREATE REQUIRED PROPERTY quantity: std::int64;
  };
};
