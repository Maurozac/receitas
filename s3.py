# -*- coding: utf-8 -*-
u""".
API para interação com AWS-S3
*****************************
Mauro Zackiewicz, Probabit, fev. 2017
"""
import boto


S3_ID = "seu_id"
S3_KEY = "sua_key"


def salvar_s3(local, arquivo, filename):
    u""".
    Salva arquivo (tipo file)
    em um local [bucket] existente na S3
    com este nome (se já existe sobrescreve)
    """
    s3 = boto.connect_s3(
        aws_access_key_id=S3_ID,
        aws_secret_access_key=S3_KEY
    )
    bucket = s3.get_bucket(local)
    key = bucket.new_key(filename)
    key.set_contents_from_file(arquivo)


def abrir_s3(local, filename):
    u""".
    Abre arquivo existente em s3
    e retorna o conteudo em forma de string
    => pronto para processar
    """
    s3 = boto.connect_s3(
        aws_access_key_id=S3_ID,
        aws_secret_access_key=S3_KEY
    )
    bucket = s3.get_bucket(local)
    k = bucket.get_key(filename)
    return k.get_contents_as_string()


def lista_files_s3(local):
    u""".
    Retorna lista de arquivos existentes em um local
    """
    s3 = boto.connect_s3(
        aws_access_key_id=S3_ID,
        aws_secret_access_key=S3_KEY
    )
    bucket = s3.get_bucket(local)
    return [key.name.encode('utf-8') for key in bucket.list()]


def arquivar_s3(local, filename, novo_local):
    u""".
    Move o file de local para novo_local
    bucket.copy_key(new_key_name, src_bucket_name, src_key_name,)
    """
    s3 = boto.connect_s3(
        aws_access_key_id=S3_ID,
        aws_secret_access_key=S3_KEY
    )
    # copiar
    para = s3.get_bucket(novo_local)
    para.copy_key(filename, local, filename)
    # apagar
    de = s3.get_bucket(local)
    de.delete_key(filename)


def apagar_s3(local, filename):
    u""".
    Apaga o file de local
    """
    s3 = boto.connect_s3(
        aws_access_key_id=S3_ID,
        aws_secret_access_key=S3_KEY
    )
    x = s3.get_bucket(local)
    x.delete_key(filename)
