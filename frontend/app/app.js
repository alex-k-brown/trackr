'use strict';

// Declare app level module which depends on views, and components
angular.module('myApp', [
  'ngRoute',
  'myApp.home',
  'myApp.add-a-goal',
  'myApp.view1',
  'myApp.view2',
  'myApp.d3graph',
  'myApp.version',
  'restangular',
   'ui.bootstrap',
   'd3',
   'myApp.detail-page'
    
]).
config(['$routeProvider', 'RestangularProvider', function($routeProvider, RestangularProvider) {
  $routeProvider.when('/add-a-goal', {
            templateUrl: 'add-a-goal/add-a-goal.html',
            controller: 'AddAGoalCtrl'
        })
  $routeProvider.when('/acheivements', {
            templateUrl: 'acheivements/acheivements.html',
            controller: 'acheivementsCtrl'
        })
  $routeProvider.otherwise({redirectTo: '/home'});
   $routeProvider.when('/detail-page', {
    templateUrl: 'detail-page/detail-page.html',
    controller: 'DetailPageCtrl'
  });
  $routeProvider.otherwise({redirectTo: '/view1'});
  RestangularProvider.setBaseUrl('http://localhost:8001');
}]);


