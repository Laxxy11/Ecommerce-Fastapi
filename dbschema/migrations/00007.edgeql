CREATE MIGRATION m16fjs2bssgv433x5imkk4pdsltgd7n7prqms5u7y3iiw4aqiq2bbq
    ONTO m1xioeotlhcwftk34y6s2s3xepuhclwd3tvnmxmhik3ux7xotk3xvq
{
  ALTER TYPE default::User {
      ALTER PROPERTY user_role {
          DROP CONSTRAINT std::exclusive;
      };
  };
};
