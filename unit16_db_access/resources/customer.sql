PGDMP     2    1            
    z            test    15.1    15.1     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16398    test    DATABASE     {   CREATE DATABASE test WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Argentina.1252';
    DROP DATABASE test;
                postgres    false            �            1259    16449    customer    TABLE     �   CREATE TABLE public.customer (
    id integer NOT NULL,
    name text,
    age integer,
    email text,
    address text,
    zip_code text
);
    DROP TABLE public.customer;
       public         heap    postgres    false            �            1259    16448    customer_id_seq    SEQUENCE     �   CREATE SEQUENCE public.customer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.customer_id_seq;
       public          postgres    false    215            �           0    0    customer_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.customer_id_seq OWNED BY public.customer.id;
          public          postgres    false    214            e           2604    16452    customer id    DEFAULT     j   ALTER TABLE ONLY public.customer ALTER COLUMN id SET DEFAULT nextval('public.customer_id_seq'::regclass);
 :   ALTER TABLE public.customer ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    214    215    215            �          0    16449    customer 
   TABLE DATA           K   COPY public.customer (id, name, age, email, address, zip_code) FROM stdin;
    public          postgres    false    215   �
       �           0    0    customer_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.customer_id_seq', 36, true);
          public          postgres    false    214            g           2606    16456    customer customer_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.customer DROP CONSTRAINT customer_pkey;
       public            postgres    false    215            �   �   x�u���0E׷_�Jy��&�"1.�L(�
%��m1$n���ə3��{���������A����y�nӠ��w�`�F�� /\�
!�PT'���O��v)�!3F)Y���VA�P6���n�%K ��y"N@6��n�RH7��6��n�8�d��;tK�������B�y"�f����dLq�     