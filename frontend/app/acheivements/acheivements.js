'use strict';

angular.module('myApp.acheivements', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/acheivements', {
    templateUrl: 'acheivements/acheivements.html',
    controller: 'acheivementsCtrl'
  });
}])

.controller('acheivementsCtrl', [function() {

}]);