# This file is transformed from CPython: Modules/_ssl_data.h
# Itself generated by Tools/ssl/make_ssl_data.py
# Generated on 2012-05-16T23:56:40.981382

from rpython.rlib import ropenssl
from rpython.rtyper.tool import rffi_platform

class CConfig:
    _compilation_info_ = ropenssl.eci

library_codes = "PEM SSL X509".split()
for code in library_codes:
    setattr(CConfig, code, rffi_platform.ConstantInteger(
        'ERR_LIB_' + code))

error_codes = [
    ('PEM', 'BAD_BASE64_DECODE'),
    ('PEM', 'BAD_DECRYPT'),
    ('PEM', 'BAD_END_LINE'),
    ('PEM', 'BAD_IV_CHARS'),
    ('PEM', 'BAD_MAGIC_NUMBER'),
    ('PEM', 'BAD_PASSWORD_READ'),
    ('PEM', 'BAD_VERSION_NUMBER'),
    ('PEM', 'BIO_WRITE_FAILURE'),
    ('PEM', 'CIPHER_IS_NULL'),
    ('PEM', 'ERROR_CONVERTING_PRIVATE_KEY'),
    ('PEM', 'EXPECTING_PRIVATE_KEY_BLOB'),
    ('PEM', 'EXPECTING_PUBLIC_KEY_BLOB'),
    ('PEM', 'INCONSISTENT_HEADER'),
    ('PEM', 'KEYBLOB_HEADER_PARSE_ERROR'),
    ('PEM', 'KEYBLOB_TOO_SHORT'),
    ('PEM', 'NOT_DEK_INFO'),
    ('PEM', 'NOT_ENCRYPTED'),
    ('PEM', 'NOT_PROC_TYPE'),
    ('PEM', 'NO_START_LINE'),
    ('PEM', 'PROBLEMS_GETTING_PASSWORD'),
    ('PEM', 'PUBLIC_KEY_NO_RSA'),
    ('PEM', 'PVK_DATA_TOO_SHORT'),
    ('PEM', 'PVK_TOO_SHORT'),
    ('PEM', 'READ_KEY'),
    ('PEM', 'SHORT_HEADER'),
    ('PEM', 'UNSUPPORTED_CIPHER'),
    ('PEM', 'UNSUPPORTED_ENCRYPTION'),
    ('PEM', 'UNSUPPORTED_KEY_COMPONENTS'),
    ('SSL', 'APP_DATA_IN_HANDSHAKE'),
    ('SSL', 'ATTEMPT_TO_REUSE_SESSION_IN_DIFFERENT_CONTEXT'),
    ('SSL', 'BAD_ALERT_RECORD'),
    ('SSL', 'BAD_AUTHENTICATION_TYPE'),
    ('SSL', 'BAD_CHANGE_CIPHER_SPEC'),
    ('SSL', 'BAD_CHECKSUM'),
    ('SSL', 'BAD_DATA_RETURNED_BY_CALLBACK'),
    ('SSL', 'BAD_DECOMPRESSION'),
    ('SSL', 'BAD_DH_G_LENGTH'),
    ('SSL', 'BAD_DH_PUB_KEY_LENGTH'),
    ('SSL', 'BAD_DH_P_LENGTH'),
    ('SSL', 'BAD_DIGEST_LENGTH'),
    ('SSL', 'BAD_DSA_SIGNATURE'),
    ('SSL', 'BAD_ECC_CERT'),
    ('SSL', 'BAD_ECDSA_SIGNATURE'),
    ('SSL', 'BAD_ECPOINT'),
    ('SSL', 'BAD_HANDSHAKE_LENGTH'),
    ('SSL', 'BAD_HELLO_REQUEST'),
    ('SSL', 'BAD_LENGTH'),
    ('SSL', 'BAD_MAC_DECODE'),
    ('SSL', 'BAD_MAC_LENGTH'),
    ('SSL', 'BAD_MESSAGE_TYPE'),
    ('SSL', 'BAD_PACKET_LENGTH'),
    ('SSL', 'BAD_PROTOCOL_VERSION_NUMBER'),
    ('SSL', 'BAD_PSK_IDENTITY_HINT_LENGTH'),
    ('SSL', 'BAD_RESPONSE_ARGUMENT'),
    ('SSL', 'BAD_RSA_DECRYPT'),
    ('SSL', 'BAD_RSA_ENCRYPT'),
    ('SSL', 'BAD_RSA_E_LENGTH'),
    ('SSL', 'BAD_RSA_MODULUS_LENGTH'),
    ('SSL', 'BAD_RSA_SIGNATURE'),
    ('SSL', 'BAD_SIGNATURE'),
    ('SSL', 'BAD_SSL_FILETYPE'),
    ('SSL', 'BAD_SSL_SESSION_ID_LENGTH'),
    ('SSL', 'BAD_STATE'),
    ('SSL', 'BAD_WRITE_RETRY'),
    ('SSL', 'BIO_NOT_SET'),
    ('SSL', 'BLOCK_CIPHER_PAD_IS_WRONG'),
    ('SSL', 'BN_LIB'),
    ('SSL', 'CA_DN_LENGTH_MISMATCH'),
    ('SSL', 'CA_DN_TOO_LONG'),
    ('SSL', 'CCS_RECEIVED_EARLY'),
    ('SSL', 'CERTIFICATE_VERIFY_FAILED'),
    ('SSL', 'CERT_LENGTH_MISMATCH'),
    ('SSL', 'CHALLENGE_IS_DIFFERENT'),
    ('SSL', 'CIPHER_CODE_WRONG_LENGTH'),
    ('SSL', 'CIPHER_OR_HASH_UNAVAILABLE'),
    ('SSL', 'CIPHER_TABLE_SRC_ERROR'),
    ('SSL', 'CLIENTHELLO_TLSEXT'),
    ('SSL', 'COMPRESSED_LENGTH_TOO_LONG'),
    ('SSL', 'COMPRESSION_DISABLED'),
    ('SSL', 'COMPRESSION_FAILURE'),
    ('SSL', 'COMPRESSION_ID_NOT_WITHIN_PRIVATE_RANGE'),
    ('SSL', 'COMPRESSION_LIBRARY_ERROR'),
    ('SSL', 'CONNECTION_ID_IS_DIFFERENT'),
    ('SSL', 'CONNECTION_TYPE_NOT_SET'),
    ('SSL', 'COOKIE_MISMATCH'),
    ('SSL', 'DATA_BETWEEN_CCS_AND_FINISHED'),
    ('SSL', 'DATA_LENGTH_TOO_LONG'),
    ('SSL', 'DECRYPTION_FAILED'),
    ('SSL', 'DECRYPTION_FAILED_OR_BAD_RECORD_MAC'),
    ('SSL', 'DH_PUBLIC_VALUE_LENGTH_IS_WRONG'),
    ('SSL', 'DIGEST_CHECK_FAILED'),
    ('SSL', 'DTLS_MESSAGE_TOO_BIG'),
    ('SSL', 'DUPLICATE_COMPRESSION_ID'),
    ('SSL', 'ECC_CERT_NOT_FOR_KEY_AGREEMENT'),
    ('SSL', 'ECC_CERT_NOT_FOR_SIGNING'),
    ('SSL', 'ECC_CERT_SHOULD_HAVE_RSA_SIGNATURE'),
    ('SSL', 'ECC_CERT_SHOULD_HAVE_SHA1_SIGNATURE'),
    ('SSL', 'ECGROUP_TOO_LARGE_FOR_CIPHER'),
    ('SSL', 'ENCRYPTED_LENGTH_TOO_LONG'),
    ('SSL', 'ERROR_GENERATING_TMP_RSA_KEY'),
    ('SSL', 'ERROR_IN_RECEIVED_CIPHER_LIST'),
    ('SSL', 'EXCESSIVE_MESSAGE_SIZE'),
    ('SSL', 'EXTRA_DATA_IN_MESSAGE'),
    ('SSL', 'GOT_A_FIN_BEFORE_A_CCS'),
    ('SSL', 'HTTPS_PROXY_REQUEST'),
    ('SSL', 'HTTP_REQUEST'),
    ('SSL', 'ILLEGAL_PADDING'),
    ('SSL', 'INCONSISTENT_COMPRESSION'),
    ('SSL', 'INVALID_CHALLENGE_LENGTH'),
    ('SSL', 'INVALID_COMMAND'),
    ('SSL', 'INVALID_COMPRESSION_ALGORITHM'),
    ('SSL', 'INVALID_PURPOSE'),
    ('SSL', 'INVALID_STATUS_RESPONSE'),
    ('SSL', 'INVALID_TICKET_KEYS_LENGTH'),
    ('SSL', 'INVALID_TRUST'),
    ('SSL', 'KEY_ARG_TOO_LONG'),
    ('SSL', 'KRB5'),
    ('SSL', 'KRB5_C_CC_PRINC'),
    ('SSL', 'KRB5_C_GET_CRED'),
    ('SSL', 'KRB5_C_INIT'),
    ('SSL', 'KRB5_C_MK_REQ'),
    ('SSL', 'KRB5_S_BAD_TICKET'),
    ('SSL', 'KRB5_S_INIT'),
    ('SSL', 'KRB5_S_RD_REQ'),
    ('SSL', 'KRB5_S_TKT_EXPIRED'),
    ('SSL', 'KRB5_S_TKT_NYV'),
    ('SSL', 'KRB5_S_TKT_SKEW'),
    ('SSL', 'LENGTH_MISMATCH'),
    ('SSL', 'LENGTH_TOO_SHORT'),
    ('SSL', 'LIBRARY_BUG'),
    ('SSL', 'LIBRARY_HAS_NO_CIPHERS'),
    ('SSL', 'MESSAGE_TOO_LONG'),
    ('SSL', 'MISSING_DH_DSA_CERT'),
    ('SSL', 'MISSING_DH_KEY'),
    ('SSL', 'MISSING_DH_RSA_CERT'),
    ('SSL', 'MISSING_DSA_SIGNING_CERT'),
    ('SSL', 'MISSING_EXPORT_TMP_DH_KEY'),
    ('SSL', 'MISSING_EXPORT_TMP_RSA_KEY'),
    ('SSL', 'MISSING_RSA_CERTIFICATE'),
    ('SSL', 'MISSING_RSA_ENCRYPTING_CERT'),
    ('SSL', 'MISSING_RSA_SIGNING_CERT'),
    ('SSL', 'MISSING_TMP_DH_KEY'),
    ('SSL', 'MISSING_TMP_ECDH_KEY'),
    ('SSL', 'MISSING_TMP_RSA_KEY'),
    ('SSL', 'MISSING_TMP_RSA_PKEY'),
    ('SSL', 'MISSING_VERIFY_MESSAGE'),
    ('SSL', 'NON_SSLV2_INITIAL_PACKET'),
    ('SSL', 'NO_CERTIFICATES_RETURNED'),
    ('SSL', 'NO_CERTIFICATE_ASSIGNED'),
    ('SSL', 'NO_CERTIFICATE_RETURNED'),
    ('SSL', 'NO_CERTIFICATE_SET'),
    ('SSL', 'NO_CERTIFICATE_SPECIFIED'),
    ('SSL', 'NO_CIPHERS_AVAILABLE'),
    ('SSL', 'NO_CIPHERS_PASSED'),
    ('SSL', 'NO_CIPHERS_SPECIFIED'),
    ('SSL', 'NO_CIPHER_LIST'),
    ('SSL', 'NO_CIPHER_MATCH'),
    ('SSL', 'NO_CLIENT_CERT_METHOD'),
    ('SSL', 'NO_CLIENT_CERT_RECEIVED'),
    ('SSL', 'NO_COMPRESSION_SPECIFIED'),
    ('SSL', 'NO_GOST_CERTIFICATE_SENT_BY_PEER'),
    ('SSL', 'NO_METHOD_SPECIFIED'),
    ('SSL', 'NO_PRIVATEKEY'),
    ('SSL', 'NO_PRIVATE_KEY_ASSIGNED'),
    ('SSL', 'NO_PROTOCOLS_AVAILABLE'),
    ('SSL', 'NO_PUBLICKEY'),
    ('SSL', 'NO_RENEGOTIATION'),
    ('SSL', 'NO_REQUIRED_DIGEST'),
    ('SSL', 'NO_SHARED_CIPHER'),
    ('SSL', 'NO_VERIFY_CALLBACK'),
    ('SSL', 'NULL_SSL_CTX'),
    ('SSL', 'NULL_SSL_METHOD_PASSED'),
    ('SSL', 'OLD_SESSION_CIPHER_NOT_RETURNED'),
    ('SSL', 'OLD_SESSION_COMPRESSION_ALGORITHM_NOT_RETURNED'),
    ('SSL', 'ONLY_TLS_ALLOWED_IN_FIPS_MODE'),
    ('SSL', 'OPAQUE_PRF_INPUT_TOO_LONG'),
    ('SSL', 'PACKET_LENGTH_TOO_LONG'),
    ('SSL', 'PARSE_TLSEXT'),
    ('SSL', 'PATH_TOO_LONG'),
    ('SSL', 'PEER_DID_NOT_RETURN_A_CERTIFICATE'),
    ('SSL', 'PEER_ERROR'),
    ('SSL', 'PEER_ERROR_CERTIFICATE'),
    ('SSL', 'PEER_ERROR_NO_CERTIFICATE'),
    ('SSL', 'PEER_ERROR_NO_CIPHER'),
    ('SSL', 'PEER_ERROR_UNSUPPORTED_CERTIFICATE_TYPE'),
    ('SSL', 'PRE_MAC_LENGTH_TOO_LONG'),
    ('SSL', 'PROBLEMS_MAPPING_CIPHER_FUNCTIONS'),
    ('SSL', 'PROTOCOL_IS_SHUTDOWN'),
    ('SSL', 'PSK_IDENTITY_NOT_FOUND'),
    ('SSL', 'PSK_NO_CLIENT_CB'),
    ('SSL', 'PSK_NO_SERVER_CB'),
    ('SSL', 'PUBLIC_KEY_ENCRYPT_ERROR'),
    ('SSL', 'PUBLIC_KEY_IS_NOT_RSA'),
    ('SSL', 'PUBLIC_KEY_NOT_RSA'),
    ('SSL', 'READ_BIO_NOT_SET'),
    ('SSL', 'READ_TIMEOUT_EXPIRED'),
    ('SSL', 'READ_WRONG_PACKET_TYPE'),
    ('SSL', 'RECORD_LENGTH_MISMATCH'),
    ('SSL', 'RECORD_TOO_LARGE'),
    ('SSL', 'RECORD_TOO_SMALL'),
    ('SSL', 'RENEGOTIATE_EXT_TOO_LONG'),
    ('SSL', 'RENEGOTIATION_ENCODING_ERR'),
    ('SSL', 'RENEGOTIATION_MISMATCH'),
    ('SSL', 'REQUIRED_CIPHER_MISSING'),
    ('SSL', 'REQUIRED_COMPRESSSION_ALGORITHM_MISSING'),
    ('SSL', 'REUSE_CERT_LENGTH_NOT_ZERO'),
    ('SSL', 'REUSE_CERT_TYPE_NOT_ZERO'),
    ('SSL', 'REUSE_CIPHER_LIST_NOT_ZERO'),
    ('SSL', 'SCSV_RECEIVED_WHEN_RENEGOTIATING'),
    ('SSL', 'SERVERHELLO_TLSEXT'),
    ('SSL', 'SESSION_ID_CONTEXT_UNINITIALIZED'),
    ('SSL', 'SHORT_READ'),
    ('SSL', 'SIGNATURE_FOR_NON_SIGNING_CERTIFICATE'),
    ('SSL', 'SSL23_DOING_SESSION_ID_REUSE'),
    ('SSL', 'SSL2_CONNECTION_ID_TOO_LONG'),
    ('SSL', 'SSL3_EXT_INVALID_ECPOINTFORMAT'),
    ('SSL', 'SSL3_EXT_INVALID_SERVERNAME'),
    ('SSL', 'SSL3_EXT_INVALID_SERVERNAME_TYPE'),
    ('SSL', 'SSL3_SESSION_ID_TOO_LONG'),
    ('SSL', 'SSL3_SESSION_ID_TOO_SHORT'),
    ('SSL', 'SSLV3_ALERT_BAD_CERTIFICATE'),
    ('SSL', 'SSLV3_ALERT_BAD_RECORD_MAC'),
    ('SSL', 'SSLV3_ALERT_CERTIFICATE_EXPIRED'),
    ('SSL', 'SSLV3_ALERT_CERTIFICATE_REVOKED'),
    ('SSL', 'SSLV3_ALERT_CERTIFICATE_UNKNOWN'),
    ('SSL', 'SSLV3_ALERT_DECOMPRESSION_FAILURE'),
    ('SSL', 'SSLV3_ALERT_HANDSHAKE_FAILURE'),
    ('SSL', 'SSLV3_ALERT_ILLEGAL_PARAMETER'),
    ('SSL', 'SSLV3_ALERT_NO_CERTIFICATE'),
    ('SSL', 'SSLV3_ALERT_UNEXPECTED_MESSAGE'),
    ('SSL', 'SSLV3_ALERT_UNSUPPORTED_CERTIFICATE'),
    ('SSL', 'SSL_CTX_HAS_NO_DEFAULT_SSL_VERSION'),
    ('SSL', 'SSL_HANDSHAKE_FAILURE'),
    ('SSL', 'SSL_LIBRARY_HAS_NO_CIPHERS'),
    ('SSL', 'SSL_SESSION_ID_CALLBACK_FAILED'),
    ('SSL', 'SSL_SESSION_ID_CONFLICT'),
    ('SSL', 'SSL_SESSION_ID_CONTEXT_TOO_LONG'),
    ('SSL', 'SSL_SESSION_ID_HAS_BAD_LENGTH'),
    ('SSL', 'SSL_SESSION_ID_IS_DIFFERENT'),
    ('SSL', 'TLSV1_ALERT_ACCESS_DENIED'),
    ('SSL', 'TLSV1_ALERT_DECODE_ERROR'),
    ('SSL', 'TLSV1_ALERT_DECRYPTION_FAILED'),
    ('SSL', 'TLSV1_ALERT_DECRYPT_ERROR'),
    ('SSL', 'TLSV1_ALERT_EXPORT_RESTRICTION'),
    ('SSL', 'TLSV1_ALERT_INSUFFICIENT_SECURITY'),
    ('SSL', 'TLSV1_ALERT_INTERNAL_ERROR'),
    ('SSL', 'TLSV1_ALERT_NO_RENEGOTIATION'),
    ('SSL', 'TLSV1_ALERT_PROTOCOL_VERSION'),
    ('SSL', 'TLSV1_ALERT_RECORD_OVERFLOW'),
    ('SSL', 'TLSV1_ALERT_UNKNOWN_CA'),
    ('SSL', 'TLSV1_ALERT_USER_CANCELLED'),
    ('SSL', 'TLSV1_BAD_CERTIFICATE_HASH_VALUE'),
    ('SSL', 'TLSV1_BAD_CERTIFICATE_STATUS_RESPONSE'),
    ('SSL', 'TLSV1_CERTIFICATE_UNOBTAINABLE'),
    ('SSL', 'TLSV1_UNRECOGNIZED_NAME'),
    ('SSL', 'TLSV1_UNSUPPORTED_EXTENSION'),
    ('SSL', 'TLS_CLIENT_CERT_REQ_WITH_ANON_CIPHER'),
    ('SSL', 'TLS_INVALID_ECPOINTFORMAT_LIST'),
    ('SSL', 'TLS_PEER_DID_NOT_RESPOND_WITH_CERTIFICATE_LIST'),
    ('SSL', 'TLS_RSA_ENCRYPTED_VALUE_LENGTH_IS_WRONG'),
    ('SSL', 'TRIED_TO_USE_UNSUPPORTED_CIPHER'),
    ('SSL', 'UNABLE_TO_DECODE_DH_CERTS'),
    ('SSL', 'UNABLE_TO_DECODE_ECDH_CERTS'),
    ('SSL', 'UNABLE_TO_EXTRACT_PUBLIC_KEY'),
    ('SSL', 'UNABLE_TO_FIND_DH_PARAMETERS'),
    ('SSL', 'UNABLE_TO_FIND_ECDH_PARAMETERS'),
    ('SSL', 'UNABLE_TO_FIND_PUBLIC_KEY_PARAMETERS'),
    ('SSL', 'UNABLE_TO_FIND_SSL_METHOD'),
    ('SSL', 'UNABLE_TO_LOAD_SSL2_MD5_ROUTINES'),
    ('SSL', 'UNABLE_TO_LOAD_SSL3_MD5_ROUTINES'),
    ('SSL', 'UNABLE_TO_LOAD_SSL3_SHA1_ROUTINES'),
    ('SSL', 'UNEXPECTED_MESSAGE'),
    ('SSL', 'UNEXPECTED_RECORD'),
    ('SSL', 'UNINITIALIZED'),
    ('SSL', 'UNKNOWN_ALERT_TYPE'),
    ('SSL', 'UNKNOWN_CERTIFICATE_TYPE'),
    ('SSL', 'UNKNOWN_CIPHER_RETURNED'),
    ('SSL', 'UNKNOWN_CIPHER_TYPE'),
    ('SSL', 'UNKNOWN_KEY_EXCHANGE_TYPE'),
    ('SSL', 'UNKNOWN_PKEY_TYPE'),
    ('SSL', 'UNKNOWN_PROTOCOL'),
    ('SSL', 'UNKNOWN_REMOTE_ERROR_TYPE'),
    ('SSL', 'UNKNOWN_SSL_VERSION'),
    ('SSL', 'UNKNOWN_STATE'),
    ('SSL', 'UNSAFE_LEGACY_RENEGOTIATION_DISABLED'),
    ('SSL', 'UNSUPPORTED_CIPHER'),
    ('SSL', 'UNSUPPORTED_COMPRESSION_ALGORITHM'),
    ('SSL', 'UNSUPPORTED_DIGEST_TYPE'),
    ('SSL', 'UNSUPPORTED_ELLIPTIC_CURVE'),
    ('SSL', 'UNSUPPORTED_PROTOCOL'),
    ('SSL', 'UNSUPPORTED_SSL_VERSION'),
    ('SSL', 'UNSUPPORTED_STATUS_TYPE'),
    ('SSL', 'WRITE_BIO_NOT_SET'),
    ('SSL', 'WRONG_CIPHER_RETURNED'),
    ('SSL', 'WRONG_MESSAGE_TYPE'),
    ('SSL', 'WRONG_NUMBER_OF_KEY_BITS'),
    ('SSL', 'WRONG_SIGNATURE_LENGTH'),
    ('SSL', 'WRONG_SIGNATURE_SIZE'),
    ('SSL', 'WRONG_SSL_VERSION'),
    ('SSL', 'WRONG_VERSION_NUMBER'),
    ('SSL', 'X509_LIB'),
    ('SSL', 'X509_VERIFICATION_SETUP_PROBLEMS'),
    ('X509', 'BAD_X509_FILETYPE'),
    ('X509', 'BASE64_DECODE_ERROR'),
    ('X509', 'CANT_CHECK_DH_KEY'),
    ('X509', 'CERT_ALREADY_IN_HASH_TABLE'),
    ('X509', 'ERR_ASN1_LIB'),
    ('X509', 'INVALID_DIRECTORY'),
    ('X509', 'INVALID_FIELD_NAME'),
    ('X509', 'INVALID_TRUST'),
    ('X509', 'KEY_TYPE_MISMATCH'),
    ('X509', 'KEY_VALUES_MISMATCH'),
    ('X509', 'LOADING_CERT_DIR'),
    ('X509', 'LOADING_DEFAULTS'),
    ('X509', 'METHOD_NOT_SUPPORTED'),
    ('X509', 'NO_CERT_SET_FOR_US_TO_VERIFY'),
    ('X509', 'PUBLIC_KEY_DECODE_ERROR'),
    ('X509', 'PUBLIC_KEY_ENCODE_ERROR'),
    ('X509', 'SHOULD_RETRY'),
    ('X509', 'UNABLE_TO_FIND_PARAMETERS_IN_CHAIN'),
    ('X509', 'UNABLE_TO_GET_CERTS_PUBLIC_KEY'),
    ('X509', 'UNKNOWN_KEY_TYPE'),
    ('X509', 'UNKNOWN_NID'),
    ('X509', 'UNKNOWN_PURPOSE_ID'),
    ('X509', 'UNKNOWN_TRUST_ID'),
    ('X509', 'UNSUPPORTED_ALGORITHM'),
    ('X509', 'WRONG_LOOKUP_TYPE'),
    ('X509', 'WRONG_TYPE'),
]
for lib, code in error_codes:
    setattr(CConfig, code, rffi_platform.DefinedConstantInteger(
        '%s_R_%s' % (lib, code)))

# Constants for ALERT_DESCRIPTION_ error codes
AD_NAMES = """
    CLOSE_NOTIFY UNEXPECTED_MESSAGE BAD_RECORD_MAC RECORD_OVERFLOW
    DECOMPRESSION_FAILURE HANDSHAKE_FAILURE BAD_CERTIFICATE
    UNSUPPORTED_CERTIFICATE CERTIFICATE_REVOKED CERTIFICATE_EXPIRED
    CERTIFICATE_UNKNOWN ILLEGAL_PARAMETER UNKNOWN_CA ACCESS_DENIED
    DECODE_ERROR DECRYPT_ERROR PROTOCOL_VERSION INSUFFICIENT_SECURITY
    INTERNAL_ERROR USER_CANCELLED NO_RENEGOTIATION UNSUPPORTED_EXTENSION
    CERTIFICATE_UNOBTAINABLE UNRECOGNIZED_NAME BAD_CERTIFICATE_STATUS_RESPONSE
    BAD_CERTIFICATE_HASH_VALUE UNKNOWN_PSK_IDENTITY
    """.split()
for name in AD_NAMES:
    setattr(CConfig, name, rffi_platform.DefinedConstantInteger(
        'SSL_AD_%s' % name))

cconfig = rffi_platform.configure(CConfig)

LIBRARY_CODES_TO_NAMES = {}
for code in library_codes:
    LIBRARY_CODES_TO_NAMES[cconfig[code]] = code
ERROR_CODES_TO_NAMES = {}
for lib, code in error_codes:
    if cconfig[code] is not None:
        ERROR_CODES_TO_NAMES[cconfig[lib], cconfig[code]] = code

ALERT_DESCRIPTION_CODES = {}
for name in AD_NAMES:
    value = cconfig[name]
    if value is not None:
        ALERT_DESCRIPTION_CODES['ALERT_DESCRIPTION_%s' % name] = value
