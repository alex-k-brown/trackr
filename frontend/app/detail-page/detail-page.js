'use strict';

angular.module('myApp.detail-page', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/detail-page', {
    templateUrl: 'detail-page/detail-page.html',
    controller: 'DetailPageCtrl'
  });
}])

.controller('DetailPageCtrl', [function() {

}]);