'use strict';

// Declare app level module which depends on views, and components
angular.module('myApp', [
  'ngRoute',
  'myApp.home',
  'myApp.addAGoal',
  'myApp.d3graph',
  'myApp.version',
  'restangular',
  'ui.bootstrap',
  'd3',
  'myApp.detail-page',
  'myApp.achievements'
    
]).
config(['$routeProvider', 'RestangularProvider', function($routeProvider, RestangularProvider) {
  $routeProvider.otherwise({redirectTo: '/home'});
  RestangularProvider.setBaseUrl('http://localhost:8001');
}]);


