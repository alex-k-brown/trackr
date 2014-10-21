'use strict';

// Declare app level module which depends on views, and components
angular.module('myApp', [
  'ngRoute',
  'myApp.home',
  'myApp.addAGoal',
  'myApp.version',
  'restangular',
  'ui.bootstrap',
  'myApp.detail-page',
  'myApp.achievements',
  'myApp.journal'

]).
config(['$routeProvider', 'RestangularProvider', function($routeProvider, RestangularProvider) {
  $routeProvider.otherwise({redirectTo: '/home'});
  RestangularProvider.setBaseUrl('http://localhost:8001');
}]);


