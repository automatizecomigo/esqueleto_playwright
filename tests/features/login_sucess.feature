# Created by rafael.pantoja at 23/07/2024
Feature: Fazer login no saucedemo, exemplo de teste

  Scenario: Fazer login com credenciais validas
    Given que o usuário acessa a página de login do saucedemo
    When o usuário preenche o campo de usuário com "standard_user" e senha com "secret_sauce"
    Then o usuário é redirecionado para a página de produtos