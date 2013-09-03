from storages.backends.s3boto import S3BotoStorage

StaticRootS3BotoStorage = lambda: S3BotoStorage(
    bucket_name='lightning-static',
    reduced_redundancy=True)

MediaRootS3BotoStorage  = lambda: S3BotoStorage(
    bucket_name='lightning-media')
# Some more defaults we may want to change later
#   auto_create_bucket = False
#   headers = {},
#   file_overwrite = True,
#   default_acl = 'public-read',
#   bucket_acl = default_acl,
#   encryption = False,
#   file_name_charset = 'utf-8')
#   gzip = False,
#   gzip_content_types = (
#        'text/css',
#        'application/javascript',
#        'application/x-javascript',
#   )

# See http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html
# for full docs
