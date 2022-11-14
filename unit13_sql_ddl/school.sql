USE [master]
GO
/****** Object:  Database [escuela]    Script Date: 3/11/2022 12:58:15 ******/
CREATE DATABASE [escuela]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'escuela', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\escuela.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'escuela_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\escuela_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO
ALTER DATABASE [escuela] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [escuela].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [escuela] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [escuela] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [escuela] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [escuela] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [escuela] SET ARITHABORT OFF 
GO
ALTER DATABASE [escuela] SET AUTO_CLOSE ON 
GO
ALTER DATABASE [escuela] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [escuela] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [escuela] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [escuela] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [escuela] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [escuela] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [escuela] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [escuela] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [escuela] SET  ENABLE_BROKER 
GO
ALTER DATABASE [escuela] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [escuela] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [escuela] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [escuela] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [escuela] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [escuela] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [escuela] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [escuela] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [escuela] SET  MULTI_USER 
GO
ALTER DATABASE [escuela] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [escuela] SET DB_CHAINING OFF 
GO
ALTER DATABASE [escuela] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [escuela] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [escuela] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [escuela] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
ALTER DATABASE [escuela] SET QUERY_STORE = OFF
GO
USE [escuela]
GO
/****** Object:  Table [dbo].[Alumno]    Script Date: 3/11/2022 12:58:15 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Alumno](
	[legajo] [varchar](10) NOT NULL,
	[nombre] [varchar](20) NOT NULL,
	[apellido] [varchar](20) NOT NULL,
	[fecha_de_nacimiento] [date] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[legajo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Cursa]    Script Date: 3/11/2022 12:58:15 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Cursa](
	[legajo] [varchar](10) NOT NULL,
	[codigo_materia] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[legajo] ASC,
	[codigo_materia] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Materia]    Script Date: 3/11/2022 12:58:15 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Materia](
	[codigo_materia] [int] IDENTITY(1,1) NOT NULL,
	[descripcion] [varchar](20) NULL,
PRIMARY KEY CLUSTERED 
(
	[codigo_materia] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Cursa]  WITH CHECK ADD  CONSTRAINT [fk_cod_materia] FOREIGN KEY([codigo_materia])
REFERENCES [dbo].[Materia] ([codigo_materia])
GO
ALTER TABLE [dbo].[Cursa] CHECK CONSTRAINT [fk_cod_materia]
GO
ALTER TABLE [dbo].[Cursa]  WITH CHECK ADD  CONSTRAINT [fk_legajo] FOREIGN KEY([legajo])
REFERENCES [dbo].[Alumno] ([legajo])
GO
ALTER TABLE [dbo].[Cursa] CHECK CONSTRAINT [fk_legajo]
GO
USE [master]
GO
ALTER DATABASE [escuela] SET  READ_WRITE 
GO
