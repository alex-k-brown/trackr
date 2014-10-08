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
//  $routeProvider.when('/achievements', {
//            templateUrl: 'achievements/achievements.html',
//            controller: 'achievementsCtrl'
//        })
//  $routeProvider.otherwise({redirectTo: '/home'});
//   $routeProvider.when('/detail-page', {
//    templateUrl: 'detail-page/detail-page.html',
//    controller: 'DetailPageCtrl'
//  });
  $routeProvider.otherwise({redirectTo: '/home'});
  RestangularProvider.setBaseUrl('http://localhost:8001');
}]);


