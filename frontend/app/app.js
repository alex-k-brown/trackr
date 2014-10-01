'use strict';

// Declare app level module which depends on views, and components
angular.module('myApp', [
  'ngRoute',
  'myApp.view1',
  'myApp.view2',
  'myApp.d3graph',
  'myApp.version',
  'restangular',
   'ui.bootstrap',
   'd3'
    
]).
config(['$routeProvider', 'RestangularProvider', function($routeProvider, RestangularProvider) {
  $routeProvider.otherwise({redirectTo: '/view1'});
  RestangularProvider.setBaseUrl('http://localhost:8001');
}]);


