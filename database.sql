create database estoque;
use estoque;

create table Fabricantes (codigo int primary key auto_increment, nome varchar (70));

create table Produtos (id int auto_increment primary key, descricao varchar(70), quantidade int);

alter table Produtos
add column codigo_fabri int, add foreign key (codigo_fabri) references Fabricantes(codigo);
select * from Produtos;
select * from Fabricantes;
insert into Produtos (descricao, quantidade, codigo_fabri) values ('Produto Normal', 5, 1);
insert into Fabricantes (codigo, nome) values (1,'Vendedor Licito');
select Produtos.descricao,nome, Produtos.codigo_fabri from Fabricantes inner join Produtos on Fabricantes.codigo = Produtos.codigo_fabri
